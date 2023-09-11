from code.the_big_program import TheBigProgram


class TestTheBigProgram:

    def test_do_some_stuff(self):
        program = TheBigProgram()
        assert "We're in Budapest!" == program.do_some_stuff()
