#include <iostream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <cassert>
using namespace std;
struct Connection{double weight; double deltaWeight;};
class Neuron;
typedef vector<Neuron> Layer;
class Neuron{
	public:
		Neuron(unsigned numOutputs, unsigned myIndex);
		void setOutputVal(double val) { m_outputVal = val; }
		double getOutputVal(void) const { return m_outputVal; }
		void fwdprop(const Layer &prevLayer);
		void calcOutputGradients(double targetVal);
    		void calcHiddenGradients(const Layer &nextLayer);
    		void updateInputWeights(Layer &prevLayer);
	private:
		static double eta;
    		static double alpha;
		static double randomWeight(void) { return rand() / double(RAND_MAX); }
		double m_outputVal;
		unsigned m_myIndex;
		static double transferFunction(double x);
    		static double transferFunctionDerivative(double x);
    		double sumDOW(const Layer &nextLayer) const;
    		vector<Connection> m_outputWeights;
    		double m_gradient;
};
double Neuron::eta = 0.5;
double Neuron::alpha = 0.0;
Neuron::Neuron(unsigned numOutputs, unsigned myIndex){
    m_outputVal = 0.0;
    m_gradient = 0.0;
    for (unsigned c = 0; c < numOutputs; c++){
        m_outputWeights.push_back(Connection());
        m_outputWeights.back().deltaWeight = 0.0;
        m_outputWeights.back().weight = randomWeight();
    }
    m_myIndex = myIndex;
}
void Neuron::fwdprop(const Layer &prevLayer){
    double sum = 0.0;
    for (unsigned n = 0; n < prevLayer.size(); n++){
        sum += prevLayer[n].getOutputVal() * prevLayer[n].m_outputWeights[m_myIndex].weight;
    }
    m_outputVal = Neuron::transferFunction(sum);
}
double Neuron::transferFunction(double x){return 1.0 / (1.0 + exp(-x));}
double Neuron::transferFunctionDerivative(double x){
    return x * (1.0 - x);
}
void Neuron::calcOutputGradients(double targetVal){
    double delta = targetVal - m_outputVal;
    m_gradient = delta * Neuron::transferFunctionDerivative(m_outputVal);
}
void Neuron::calcHiddenGradients(const Layer &nextLayer){
    double dow = sumDOW(nextLayer);
    m_gradient = dow * Neuron::transferFunctionDerivative(m_outputVal);
}
double Neuron::sumDOW(const Layer &nextLayer) const{
    double sum = 0.0;
    for (unsigned n = 0; n < nextLayer.size() - 1; ++n) {
        sum += m_outputWeights[n].weight * nextLayer[n].m_gradient;
    }
    return sum;
}
void Neuron::updateInputWeights(Layer &prevLayer){
    for (unsigned n = 0; n < prevLayer.size(); ++n) {
        Neuron &neuron = prevLayer[n];
        double oldDeltaWeight = neuron.m_outputWeights[m_myIndex].deltaWeight;
        double newDeltaWeight = eta * neuron.getOutputVal() * m_gradient + alpha * oldDeltaWeight;
        neuron.m_outputWeights[m_myIndex].deltaWeight = newDeltaWeight;
        neuron.m_outputWeights[m_myIndex].weight += newDeltaWeight;
    }
}
class NeuralNet{
	public:
		NeuralNet(const vector<unsigned> &topology);
		void fwdprop(const vector<double> &InputVals);
		void backprop(const vector<double> &TargetVals);
		void results(vector<double> &resultVals) const;
		double getRecentAverageError() const;
	private:
		vector<Layer> m_layers;
		vector<Connection> m_outputWeights;
		double m_error;
		double m_recentAverageError;
    		static double m_recentAverageSmoothingFactor;
};
NeuralNet::NeuralNet(const vector<unsigned> &topology){
    m_error = 0.0; m_recentAverageError = 0.0;
    unsigned numLayers = topology.size();
    for (unsigned layerNum = 0; layerNum < numLayers; layerNum++){
        m_layers.push_back(Layer());
        unsigned numOutputs = layerNum == topology.size() - 1 ? 0 : topology[layerNum + 1];
        for (unsigned neuronNum = 0; neuronNum <= topology[layerNum]; neuronNum++) {
            m_layers.back().push_back(Neuron(numOutputs, neuronNum));
            cout << "Made Neuron " << layerNum << " " << neuronNum << endl;
        }
        m_layers.back().back().setOutputVal(1.0);
    }
};
double NeuralNet::m_recentAverageSmoothingFactor = 100.0;
void NeuralNet::fwdprop(const vector<double> &InputVals){
    assert(InputVals.size() == m_layers[0].size() - 1);
    for (unsigned i = 0; i < InputVals.size(); ++i) {
        m_layers[0][i].setOutputVal(InputVals[i]);
    }
    for (unsigned layerNum = 1; layerNum < m_layers.size(); ++layerNum) {
        Layer &prevLayer = m_layers[layerNum - 1];
        for (unsigned n = 0; n < m_layers[layerNum].size() - 1; ++n) {
            m_layers[layerNum][n].fwdprop(prevLayer);
        }
    }
}
void NeuralNet::backprop(const vector<double> &TargetVals){
    Layer &outputLayer = m_layers.back();
    m_error = 0.0;
    for (unsigned n = 0; n < outputLayer.size() - 1; ++n) {
        double delta = TargetVals[n] - outputLayer[n].getOutputVal();
        m_error += delta * delta;
    }
    m_error /= outputLayer.size() - 1;
    m_recentAverageError = (m_recentAverageError * m_recentAverageSmoothingFactor + m_error) / (m_recentAverageSmoothingFactor + 1.0);

    for (unsigned n = 0; n < outputLayer.size() - 1; ++n) {
        outputLayer[n].calcOutputGradients(TargetVals[n]);
    }

    for (unsigned layerNum = m_layers.size() - 2; layerNum > 0; --layerNum) {
        Layer &hiddenLayer = m_layers[layerNum];
        Layer &nextLayer = m_layers[layerNum + 1];
        for (unsigned n = 0; n < hiddenLayer.size(); ++n) {
            hiddenLayer[n].calcHiddenGradients(nextLayer);
        }
    }

    for (unsigned layerNum = m_layers.size() - 1; layerNum > 0; --layerNum) {
        Layer &layer = m_layers[layerNum];
        Layer &prevLayer = m_layers[layerNum - 1];
        for (unsigned n = 0; n < layer.size() - 1; ++n) {
            layer[n].updateInputWeights(prevLayer);
        }
    }
}
void NeuralNet::results(vector<double> &resultVals) const{
    resultVals.clear();
    for (unsigned n = 0; n < m_layers.back().size() - 1; ++n) {
        resultVals.push_back(m_layers.back()[n].getOutputVal());
    }
}
double NeuralNet::getRecentAverageError() const{
    return m_recentAverageError;
}
int main(){
    srand(42);
    vector<unsigned> topology = {2, 2, 1};
    NeuralNet Net(topology);
    vector<vector<double>> InputVals = {{0.0, 0.0},{0.0, 1.0},{1.0, 0.0},{1.0, 1.0}};
    vector<vector<double>> TargetVals = {{0.0},{0.0},{0.0},{1.0}};
    vector<double> resultVals;
    double initialLoss = 0.0;
    for (unsigned epoch = 0; epoch < 5000; ++epoch){
        for (unsigned sample = 0; sample < InputVals.size(); ++sample){
            Net.fwdprop(InputVals[sample]);
            Net.backprop(TargetVals[sample]);
        }
        if (epoch == 0){
            initialLoss = Net.getRecentAverageError();
        }
        if (epoch % 500 == 0){
            cout << "Epoch: " << epoch << " | Loss: " << Net.getRecentAverageError() << endl;
        }
    }
    double finalLoss = Net.getRecentAverageError();
    cout << "\nInitial Loss: " << initialLoss << endl;
    cout << "Final Loss:   " << finalLoss << endl;
    if (finalLoss < initialLoss){
        cout << "PASS: Loss decreased." << endl;
    } else {
        cout << "FAIL: Loss did not decrease." << endl;
    }
    cout << "\nFinal predictions:\n";
    bool predictionsPass = true;
    for (unsigned sample = 0; sample < InputVals.size(); ++sample){
        Net.fwdprop(InputVals[sample]);
        Net.results(resultVals);
        double prediction = resultVals[0];
        double target = TargetVals[sample][0];
        cout << InputVals[sample][0] << " AND " << InputVals[sample][1] << " -> " << prediction << " (target = " << target << ")" << endl;
        if (fabs(prediction - target) > 0.1){
            predictionsPass = false;
        }
    }
    if (predictionsPass){cout << "PASS: All outputs are within 0.1 of targets." << endl;
    } else {cout << "FAIL: Outputs exceed 0.1 tolerance." << endl; }
    return 0;
}
