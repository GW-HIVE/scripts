class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: parse_list
baseCommand:
  - python
inputs:
  - id: to_parse
    type: File
    inputBinding:
      position: 0
  - id: script
    type: File
    inputBinding:
      position: -1
outputs:
  - id: parsed_file
    type: File
    outputBinding:
      glob: dict.txt
arguments:
  - position: 0
    valueFrom: '-i'
  - position: 2
    prefix: '-k'
    valueFrom: '1'
  - position: 3
    prefix: '-v'
    valueFrom: '2'
  - position: 4
    prefix: '-d'
    valueFrom: '; '
requirements:
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.to_parse)
      - $(inputs.script)
  - class: InlineJavascriptRequirement
stdout: dict.txt
