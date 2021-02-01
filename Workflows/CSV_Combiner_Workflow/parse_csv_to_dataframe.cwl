class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: parse_file
baseCommand:
  - python 
inputs:
  - id: to_parse
    type: File
    inputBinding:
      position: 2
  - id: script
    type: File
    inputBinding:
        position: 0
outputs:
  - id: parsed_file
    type: File
    outputBinding:
      glob: parsed_file.txt
arguments:
  - position: 1
    valueFrom: '-i'
requirements:
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.to_parse)
      - $(inputs.script)
  - class: InlineJavascriptRequirement
stdout: parsed_file.txt
