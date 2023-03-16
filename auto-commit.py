import os

def git_add_and_commit():
  try:
    print(os.popen("git status").read())
    print(os.popen("git add .").read())
    print(os.popen('git commit -m "auto commit"').read())
  except:
    print("Error: Somethings went wrong in add & commit.")

def git_auto_commit():
  git_add_and_commit()
  try:
    print(os.popen("git push").read())
  except:
    print("Error: Somethings went wrong in push.")

if __name__ == "__main__":
  git_auto_commit()
  input("Press any key to exit!")