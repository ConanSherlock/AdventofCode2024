def runCondaWin(command) {
    def processCheck = """${bat(returnStatus: true,
   script: '''
               call conda activate cs_aoc
               call ''' + command + '''
           '''
   )}"""

    return processCheck
}

def runVenvUnix(command) {
    def processCheck = """${bash(returnStatus: true,
   script: '''
               source /venv/Scripts/activate
               ''' command '''
           '''
   )}"""

    return processCheck
}

return this