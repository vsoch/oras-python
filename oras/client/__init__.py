#!/usr/bin/env python

__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MIT"

import oras
from oras.logger import setup_logger
import oras.client.help as help
import argparse
import sys
import os


def get_parser():
    parser = argparse.ArgumentParser(
        description="OCI Registry as Storage Python client",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--quiet",
        dest="quiet",
        help="suppress additional output.",
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "--version",
        dest="version",
        help="Show the oras version information.",
        default=False,
        action="store_true",
    )

    description = "actions for ORAS Python"
    subparsers = parser.add_subparsers(
        help="oras actions",
        title="actions",
        description=description,
        dest="command",
        required=True,
    )

    # print version and exit
    subparsers.add_parser("version", description="show software version")

    # Login
    login = subparsers.add_parser(
        "login",
        description=help.login_help,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    logout = subparsers.add_parser("logout", description="logout from a registry")

    login.add_argument(
        "--password-stdin",
        dest="password_stdin",
        help="read password or identity token from stdin",
        default=False,
        action="store_true",
    )

    # Login and logout share config and hostname arguments
    for command in [login, logout]:
        command.add_argument("hostname", help="hostname")
    
    # Debug is added on the level of the command
    for command in [login, logout, push]:
        command.add_argument(
            "--debug",
            dest="debug",
            help="debug mode",
            default=False,
            action="store_true",
        )

    # Copy command
    copy = subparsers.add_parser("copy", description=help.copy_help)
    copy.add_argument("--manifest-config", help="manifest config file")

    copy_required = copy.add_argument_group('required arguments for copy')
    copy_required.add_argument("--from", dest="from_str", help="source type and possible options", required=True)
    copy_required.add_argument("--to", dest="to_str", help="destination type and possible options", required=True)
  
    pull = subparsers.add_parser("pull", description="pull a container")

    push = subparsers.add_parser("push", description=help.push_help)
    push.add_argument("target", help="target")
    push.add_argument("filerefs", help="file references", nargs="*")
    push.add_argument("--manifest-config", help="manifest config file")
    push.add_argument("--manifest-path-validation", help="manifest annotation file")
    push.add_argument("--disable-path-validation", help="skip path validation", default=False, action="store_true")
    push.add_argument("-v", "--verbose", help="verbose output", default=False, action="store_true")

    for command in [push, copy]:
        command.add_argument("--manifest-config", help="manifest config file")
        command.add_argument("--plain-http", help="use plain http and not https", default=False, action="store_true")
    
    for command in [login, logout, push, copy]
        command.add_argument(
          "-c",
          "--config",
          dest="config",
          help="auth config path",
      )

    # login and push share username/password, and insecure
    for command in [login, push, copy]:     
        command.add_argument("-u", "--username", dest="username", help="registry username")
        command.add_argument(
        "-p", "--password", dest="password", help="registry password or identity token")
        command.add_argument(
            "-k",
            "--insecure",
            dest="insecure",
            help="allow connections to SSL registry without certs",
            default=False,
            action="store_true",
        )

    shell = subparsers.add_parser("shell", description="create an interactive shell")
    return parser


def run():
    """
    Entrypoint to OCI Python
    """
    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    def help(return_code=0):
        version = oras.__version__

        print("\nOCI Registry as Storage (oras) Python Client v%s" % version)
        parser.print_help()
        sys.exit(return_code)

    # retrieve subparser (with help) from parser
    helper = None
    subparsers_actions = [
        action
        for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)
    ]
    for subparsers_action in subparsers_actions:
        for choice, subparser in subparsers_action.choices.items():
            if choice == args.command:
                helper = subparser

    if args.debug:
        os.environ["MESSAGELEVEL"] = "DEBUG"

    setup_logger(quiet=args.quiet, debug=args.debug, verbose=getattr(args, "verbose", False))

    # Direct to the right parser
    if args.command == "version" or args.version:
        from .version import main
    elif args.command == "copy":
        from .copy import main
    elif args.command == "login":
        from .login import main
    elif args.command == "logout":
        from .logout import main
    elif args.command == "pull":
        from .pull import main
    elif args.command == "push":
        from .push import main
    elif args.command == "shell":
        from .shell import main

    # Pass on to the correct parser
    return_code = 0
    #try:
    main(args=args, parser=parser, extra=extra, subparser=helper)
    sys.exit(return_code)
    #except UnboundLocalError:
    #    return_code = 1

    help(return_code)


if __name__ == "__main__":
    run()
