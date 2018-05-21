import Executor
from File import DEFAULT_FILE_INFO


def script(name, stdInput = None, fileInput = DEFAULT_FILE_INFO, stdOutput = None, fileOutput = DEFAULT_FILE_INFO):
    with fileInput.exists():
        fileInput.write(fileInput.data)
        with fileOutput.exists():
            with Executor.run(name) as process:
                stdout, stderr = process.communicate(stdInput)
                assert not stderr, 'There is some errors while script {} was executing: {}'.format(name, stderr)
                assert process.returncode == 0, 'Script {} finished with exit code {}'.format(name, process.returncode)
                assert stdOutput is None or stdout.strip() == stdOutput, 'Script {} output does not match expected.\nExpected: {}\nGot: {}'.format(name, stdOutput, stdout)
                if fileOutput != DEFAULT_FILE_INFO:
                    fileOutputData = fileOutput.read()
                    assert fileOutputData.strip() == fileOutput.data, 'Script {} file {} output does not match expected.\nExpected: {}\nGot: {}'.format(name, fileOutput.name, fileOutput.data, fileOutputData)
