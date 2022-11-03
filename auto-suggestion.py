#!/usr/bin/env python
"""
Simple example of a CLI that demonstrates fish-style auto suggestion.
When you type some input, it will match the input against the history. If One
entry of the history starts with the given input, then it will show the
remaining part as a suggestion. Pressing the right arrow will insert this
suggestion.
"""
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import InMemoryHistory


def main():
    # Create some history first. (Easy for testing.)
    history = InMemoryHistory()
    history.append_string("create database ")
    history.append_string('create table')
    history.append_string('show databases')
    history.append_string("show tables")
    history.append_string("use ")
    history.append_string("drop database ")

    # Print help.
    print("This CLI has fish-style auto-suggestion enable.")
    print('Type for instance "pri", then you\'ll see a suggestion.')
    print("Press the right arrow to insert the suggestion.")
    print("Press Control-C to retry. Control-D to exit.")
    print()

    session = PromptSession(
        history=history,
        auto_suggest=AutoSuggestFromHistory(),
        enable_history_search=True,
    )

    while True:
        try:
            text = session.prompt("Say something: ")
        except KeyboardInterrupt:
            pass  # Ctrl-C pressed. Try again.
        else:
            break

    print("You said: %s" % text)


if __name__ == "__main__":
    main()
