# hi

this is a repository for hosting my random p5 projects at one place
> if you like clean code, please dont open the sources.

# what does it contain ?

each folder is a separate p5 project, except `lib` which contains javascript libraries
```
lib
├── p5.js
└── p5.sound.js
```

there is a file `manage.py` at the root, which manages the projects
```bash
$ ./manage.py
usage:
        manage create [project_name]
        manage serve
        manage serve [project_name]
```
> currently it is very limited, but I have plans to add more functionality with time

the `random_p5_projects.sublime-project` file contains sublime specific settings and build systems
and lastly `index.html` which I dont really know why I added, but still made it cos it feels important

