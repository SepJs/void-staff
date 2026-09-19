class BaseModule:
    def __init__(self):
        self.name = "Base Module"
        self.description = "Default description"
        self.author = "Unknown"
        # Option structure: 'OPTION_NAME': [default_value, is_required, 'description']
        self.options = {}

    def set_option(self, key, value):
        key = key.upper()
        if key in self.options:
            self.options[key][0] = value
            print(f"[+] {key} => {value}")
        else:
            print(f"[-] Invalid option: {key}")

    def show_options(self):
        print("\nModule Options:")
        print(f"{'Option':<15} {'Value':<20} {'Required':<10} {'Description':<30}")
        print("-" * 75)
        for key, val in self.options.items():
            value_str = str(val[0]) if val[0] is not None else ""
            req_str = "yes" if val[1] else "no"
            desc_str = str(val[2])
            print(f"{key:<15} {value_str:<20} {req_str:<10} {desc_str:<30}")
        print()

    def run(self):
        """Must be implemented by child modules."""
        raise NotImplementedError("The 'run' method must be implemented by the module.")