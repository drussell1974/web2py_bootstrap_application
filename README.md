# web2py_bootstrap_application
bootstrap_template scaffold application for web2py

# setup for development

For development create two folders: The repository and the web2py framework

1. Create dev folder

```mkdir dev```
```cd dev```

2. Clone the web2py_bootstrap_template source code to your local machine

```git clone https://github.com/drussell1974/web2py_bootstrap_application.git```

3. Download to dev folder https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip

4. Extract zip

```
ROOT
- dev
    |- web2py_bootstrap_application <repository>
        |- src
            |- _bootstrap_template_
    |- web2py_src <extracted>
        |- web2py
            |- applications
                |- _bootstrap_template_
```

# yarn 

Use yarn to create packages e.g. unit test and deploy application to web2py/applications

See yarn docs:

https://classic.yarnpkg.com/en/docs/usage

https://classic.yarnpkg.com/lang/en/docs/cli/run/

## tasks

*Unit Test*

TODO: Test application

``` yarn run unittest ```

*Deploy*

1. TODO: Test application
2. Copy to ../web2py_src/web2py/applications

``` yarn run deploy ```

*Build*

TODO: Test application and create zip and tar files

``` yarn run build ```
