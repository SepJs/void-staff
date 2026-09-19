import sys
from core.loader import load_modules

BANNER = r"""
 __      __      _       _    _____  _              __  __ 
 \ \    / /     (_)     | |  / ____|| |            / _|/ _|
  \ \  / /___    _   __| | | (___  | |_  __ _  | |_| |_ 
   \ \/ // _ \  | | / _` |  \___ \ | __|/ _` | |  _|  _|
    \  /| (_) | | || (_| |  ____) || |_| (_| | | | | |  
     \/  \___/  |_| \__,_| |_____/  \__|\__,_| |_| |_|  
                                 [ Modular Framework v1.0 ]
"""

class VoidStaffCLI:
    def __init__(self):
        self.modules = load_modules()
        self.current_module = None
        self.current_module_name = None

    def start(self):
        print("\033[95m" + BANNER + "\033[0m")
        print(f"[*] Loaded {len(self.modules)} module(s). Type 'help' for available commands.\n")

        while True:
            try:
                if self.current_module:
                    prompt = f"\033[91mvoid_staff\033[0m (\033[93m{self.current_module_name}\033[0m) > "
                else:
                    prompt = "\033[91mvoid_staff\033[0m > "

                user_input = input(prompt).strip()
                if not user_input:
                    continue

                parts = user_input.split()
                cmd = parts[0].lower()
                args = parts[1:]

                self.handle_command(cmd, args)

            except KeyboardInterrupt:
                print("\n[*] Use 'exit' command to quit.")
            except EOFError:
                break

    def handle_command(self, cmd, args):
        if cmd in ["exit", "quit"]:
            print("[*] Exiting Void Staff...")
            sys.exit(0)

        elif cmd == "help":
            self.show_help()

        elif cmd in ["modules", "show_modules"]:
            print("\nAvailable Modules:")
            for name, mod in self.modules.items():
                print(f"  - \033[92m{name:<15}\033[0m : {mod.description}")
            print()

        elif cmd == "use":
            if not args:
                print("[-] Usage: use <module_name>")
                return
            mod_name = args[0]
            if mod_name in self.modules:
                self.current_module_name = mod_name
                self.current_module = self.modules[mod_name]
                print(f"[*] Active module set to: {mod_name}")
            else:
                print(f"[-] Module '{mod_name}' not found.")

        elif cmd == "back":
            if self.current_module:
                self.current_module = None
                self.current_module_name = None
            else:
                print("[-] Already at root console.")

        elif cmd in ["options", "show_options"]:
            if self.current_module:
                self.current_module.show_options()
            else:
                print("[-] No active module. Select one using 'use <module_name>'.")

        elif cmd == "set":
            if not self.current_module:
                print("[-] No active module selected.")
                return
            if len(args) < 2:
                print("[-] Usage: set <OPTION> <VALUE>")
                return
            key = args[0]
            value = " ".join(args[1:])
            self.current_module.set_option(key, value)

        elif cmd in ["run", "execute"]:
            if self.current_module:
                try:
                    self.current_module.run()
                except Exception as e:
                    print(f"[!] Execution failed: {e}")
            else:
                print("[-] No active module selected.")

        else:
            print(f"[-] Unknown command: '{cmd}'. Type 'help' for usage.")

    def show_help(self):
        print("""
Global Commands:
  help               Show this help menu
  modules            List all loaded modules
  use <name>         Select and interact with a module
  exit / quit        Exit the console

Module Context Commands:
  options            Display configurable options for active module
  set <KEY> <VAL>    Set option value
  run / execute      Run active module
  back               Return to main menu
""")

if __name__ == "__main__":
    app = VoidStaffCLI()
    app.start()