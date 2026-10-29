

<tool_use>
<function name="bash">
<parameter name="command">python3 -I -c "import scipy; print('scipy', scipy.__version__)" 2>&1; python3 -I -c "import ortools; print('ortools')" 2>&1; python3 -I -c "import networkx; print('networkx', networkx.__version__)" 2>&1; which minisat glucose kissat z3 2>&1</parameter>
<parameter name="description">Check available solvers/packages</parameter>
</invoke>
</function>