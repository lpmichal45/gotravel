#! /usr/bin/python3

import connexion

def main():
    app = connexion.App('gotravel')
    app.add_api('api.yml')
    app.run(port=8080)

if __name__ == '__main__':
    main()
