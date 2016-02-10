import os, sys

# Confirm that there are is a location given
if len(sys.argv) < 3:
   print 'Please specify a location'
   sys.exit()
if len(sys.argv) > 3:
   print 'Please specify ONE location'
   sys.exit()

# Set the location of the new project
if os.path.exists(sys.argv[1]):
   location = sys.argv[1]
   project_name = sys.argv[2]
   print 'All good', location
else:
   print 'Please specify a VALID location'
   sys.exit()

# Make the root folder
project_dir = location + '/' + project_name
os.mkdir(project_dir)

# Append the new folders
new_dirs = [
   project_dir + '/scripts',
   project_dir + '/data',
   project_dir + '/styles',
   project_dir + '/scripts/libs'
]

for dir in new_dirs:
   os.mkdir(dir)

# Append the new files
new_files = [
   project_dir + '/scripts/script.js',
   project_dir + '/styles/style.scss',
   project_dir + '/index.html'
]

for file in new_files:
   open(file, 'wt')