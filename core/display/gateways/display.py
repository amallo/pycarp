"""
Display port: feedback to the user (e.g. startup stages, ready, errors).
"""


class Display:
    """Port: display feedback (e.g. startup stages, ready, errors)."""

    def show_stage(self, label):
        """Show a step in progress. label: short string (e.g. 'Init', 'Device')."""
        raise NotImplementedError

    def show_ready(self):
        """Show startup complete (e.g. 'Ready')."""
        raise NotImplementedError

    def show_error(self, msg):
        """Show error. msg: short string (e.g. 'Err NVS')."""
        raise NotImplementedError

    def clear(self):
        """Clear the display."""
        raise NotImplementedError
