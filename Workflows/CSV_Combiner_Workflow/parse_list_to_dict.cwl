class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: parse_list
baseCommand:
  - python ../python/list_to_dict.py
inputs:
  - id: to_parse
    type: File
    inputBinding:
      position: 0
outputs:
  - id: parsed_file
    type: File
    outputBinding:
      glob: dict.txt
arguments:
  - position: 0
    prefix: ''
    valueFrom: '-i'
  - position: 2
    prefix: '-k'
    valueFrom: '1'
  - position: 3
    prefix: '-v'
    valueFrom: '2'
  - position: 0
    prefix: '-d'
    valueFrom: '; '
requirements:
  - class: DockerRequirement
    dockerOutputDirectory: \src
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.to_parse)
  - class: InlineJavascriptRequirement
stdout: dict.txt
