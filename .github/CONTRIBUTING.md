# Contributing

## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Running](#running)
* [Testing](#testing)
* [Style](#style)

## Requirements

1. [Homebrew](http://brew.sh) for managing software packages on OS X
    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

2. [git](https://git-scm.com) for version control
    ```
    brew install git
    ```

3. [Homebrew Bundle](https://github.com/Homebrew/homebrew-bundle) for bundling packages with Homebrew
    ```
    brew tap Homebrew/bundle
    ```

4. [Docker for Mac](https://docs.docker.com/docker-for-mac/)

## Installation

1. Clone this repo
    ```
    git clone git@github.com:mdzhang/grpc_python_example.git
    cd grpc_python_example
    ```

2. Install Homebrew packages
    ```
    brew bundle
    ```

3. Add `pyenv init` to your shell to enable shims and autocompletion
    ```
    # ~/.bashrc

    if which pyenv > /dev/null; then
      eval "$(pyenv init -)"
    fi

    if which pyenv-virtualenv > /dev/null; then
      eval "$(pyenv virtualenv-init -)";
      export PYENV_VIRTUALENV_DISABLE_PROMPT=1
    fi

    if which direnv > /dev/null; then
      eval "$(direnv hook bash)"
    fi
    ```

4. Restart shell so that changes take effect
    ```
    source ~/.bashrc
    ```

3. Install Python
    ```
    pyenv install -s $(cat ./.python-version)
    ```

4. Create virtual environment
    ```
    pyenv virtualenv grpc_python_example
    pyenv activate grpc_python_example
    ```

5. Install Python packages
    ```
    make install
    ```

6. Install git hooks
    ```
    pre-commit install
    ```

7. Install development environment variables
    ```
    cp .envrc.dev .envrc
    direnv allow
    ```

## Running

1. Bring database up
    ```
    make up
    ```

2. Run server
    ```
    make run-server
    ```

3. Run text client
    ```
    make run-text-client ARGS="check_health"
    ```

## Testing

TODO

## Style

* Must pass `pylint`
* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/)
