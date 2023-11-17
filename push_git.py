import os
import time
import subprocess

def push_code_git():
    template_folder = os.path.dirname(os.path.abspath(__file__))
    git_add = ["git", "add", "."]
    git_commit = ["git", "commit", "-m", str(int(time.time()))]
    git_push = ["git", "push"]
    try:
        subprocess.run(git_add, check=True, cwd=template_folder)
        subprocess.run(git_commit, check=True, cwd=template_folder)
        subprocess.run(git_push, check=True, cwd=template_folder)
        print("Git add, commit, and push successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def main():
    print('Push code...')
    push_code_git()

if __name__ == '__main__':
    main()