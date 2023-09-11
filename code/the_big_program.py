class TheBigProgram:
    _city = "Budapest"

    def do_some_stuff(self) -> str:
        output = f"We're in {self._city}!"
        print(output)
        return output


if __name__ == "__main__":
    TheBigProgram().do_some_stuff()
