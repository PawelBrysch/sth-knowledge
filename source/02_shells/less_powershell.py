"""filter output"""
<some command> | sls <some_string_to_find>

"""select customisation - example"""
Get-Process | select Id, ProcessName

"""write output of one command to another"""
<command> $(<other command>)