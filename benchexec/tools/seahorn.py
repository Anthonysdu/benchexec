# This file is part of BenchExec, a framework for reliable benchmarking:
# https://github.com/sosy-lab/benchexec
#
# SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
# SPDX-FileCopyrightText: 2015 Carnegie Mellon University
#
# SPDX-License-Identifier: LicenseRef-BSD-3-Clause-CMU

# SeaHorn Verification Framework
# DM-0002198

import benchexec.tools.template
import benchexec.result as result


class Tool(benchexec.tools.template.BaseTool2):
    REQUIRED_PATHS = ["bin", "crab", "include", "lib", "share"]

    def executable(self, tool_locator):
        return tool_locator.find_executable("sea", subdir="bin")

    def program_files(self, executable):
        return self._program_files_from_executable(
            executable, self.REQUIRED_PATHS, parent_dir=True
        )

    def name(self):
        return "SeaHorn"

    def project_url(self):
        return "https://github.com/seahorn/seahorn"

    def cmdline(self, executable, options, task, rlimits):
        return [executable] + options + [task.single_input_file]

    def version(self, executable):
        return self._version_from_tool(
            f"{str(executable)}horn", line_prefix="  SeaHorn version"
        )

    def determine_result(self, run):
        if run.output[-1].startswith("sat"):
            return result.RESULT_FALSE_PROP
        if run.output[-1].startswith("unsat"):
            return result.RESULT_TRUE_PROP
        return result.RESULT_ERROR
