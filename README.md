# phaser_lessons
lessons from the boilerplates for teaching games programming using drussell1974/phaser_edu

# Creating content

## Structure

- Use feature branches to develop code

```
 - master/
    |- dev/
        |- feature/<name>/
```

- Use the template to create a directory in source

```
<name>
    |- activity
        | - web2py.<name>.activity.w2p
    |- solution
        | - web2py.<name>.solution.w2p
```

## Creating a new feature branch

1. Checkout the dev branch

```
git checkout dev
git pull
```

2. Create a new feature branch from the dev branch

``` git branch feature/<name> ```

## Create your directory in the src folder for your game

3. Use the following command to create a directory

After running the command you will be prompted to enter a name (no spaces - use underscore)

``` yarn run create_activity ```

### Change the name shown in the browser tab

Show the name of your activity shown in the browser tab by editing the title in the index.html

1. Open the index.html
2. Update the e.g. <title>Use collision detection</title>

```
<!doctype html> 
<html lang="en"> 
<head> 
    <meta charset="UTF-8" />
    <!-- feature title -->
    <title>Create an animated sprite</title>
    <!-- get the phaser3 framework when page is loading -->
    <script src="//cdn.jsdelivr.net/npm/phaser@3.11.0/dist/phaser.js"></script>
    <style type="text/css">
        body {
            margin: 0;
        }
    </style>
</head>
<body>

    <!-- Load the game from the javascript file game.js -->
    <!-- This is run in the body after page has loaded -->
    <script src="js/game.js"></script>

</body>
</html>
```

### Change the configuration for the game accordingly

3. Open js/game.js 

```
var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};
```
