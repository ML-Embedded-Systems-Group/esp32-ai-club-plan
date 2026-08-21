## Git and GitHub Workflow

All members must use Git properly so that changes are easy to review and nobody directly modifies the `main` branch.

### 1. Clone the Repository

```bash
git clone ML-Embedded-Systems-Group/esp32-ai-club-plan.git
cd esp32-ai-club-plan
```

### 2. Create Your Own Branch

Never work directly on `main`. Update your local repository first, then create a branch for your task.

```bash
git checkout main
git pull origin main
git checkout -b week1-<task-id>-<your-name>
```

Example:

```bash
git checkout -b week1-r2-soham
```

### 3. Complete Your Task

Work only on your assigned task. Add your report, reproduction script, and required evidence.

Before committing, check your changes:

```bash
git status
git diff
```

Do not commit credentials, API keys, virtual environments, build outputs, or unnecessary generated files.

### 4. Commit Your Work

Stage only the files related to your task.

```bash
git add <files>
git commit -m "complete R2 gradient descent task"
```

Use short and meaningful commit messages.

### 5. Update Your Branch

Before submitting, update your branch with the latest `main`:

```bash
git fetch origin
git rebase origin/main
```

If there is a conflict, resolve it carefully, test your work again, then continue:

```bash
git add <resolved-files>
git rebase --continue
```

### 6. Push Your Branch

```bash
git push -u origin week1-<task-id>-<your-name>
```

If you already pushed the branch before rebasing:

```bash
git push --force-with-lease
```

Do not use plain `--force`.

### 7. Open a Pull Request

Open a Pull Request from your branch into `main`.

The Pull Request should include:

- Task ID and topic.
- Short description of the completed work.
- Issue Link.
- Important output or result.
- Any remaining questions or problems.

Do not merge the Pull Request immediately.

### 8. Pair Review

Ask your assigned pair to review the Pull Request.

The reviewer should check:

- [ ] Explanation is written in the member's own words.
- [ ] Maths or reasoning is correct.
- [ ] Reproduction script runs successfully.
- [ ] Reported output matches the actual output.
- [ ] Report follows the task requirements.
- [ ] No unrelated files were changed.
- [ ] No credentials or generated files were committed.

Fix any review comments and push the changes to the same branch. The Pull Request will update automatically.

### 9. Merge After Review

Merge the Pull Request only after the required review is complete.

After the PR is merged:

```bash
git checkout main
git pull origin main
git branch -d week1-<task-id>-<your-name>
```

### Git Workflow Summary

```text
main
  ↓
create task branch
  ↓
complete task
  ↓
test and verify
  ↓
commit
  ↓
rebase on latest main
  ↓
push
  ↓
open Pull Request
  ↓
pair review
  ↓
fix review comments
  ↓
merge into main
```

**Never push task work directly to `main`. All Week 1 submissions must go through a task branch and Pull Request.**
