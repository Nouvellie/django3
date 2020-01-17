# REACT
## Install
#### Node:

```sh
$ brew install node
```

#### React app:

```sh
$ npm install -g create-react-app
```

#### Create frontend:

```sh
$ create-react-app django-react-test1
```

## Delete src files

```sh
$ sudo rm -rf django-react-test1/src
$ touch django-react-test1/src/index.js
```

## Install bootstraps

```sh
$ npm install bootstrap@4.4.1
$ npm install reactstratp@8.3.2
```

#### If reactstrap get errors:

```sh
$ npm install jquery@1.9.1
$ npm install typescript@2.8.0
$ npm install tsutils@3.17.1
```

#### Fix vulnerabilities:

```sh
$ npm audit fix -f
```