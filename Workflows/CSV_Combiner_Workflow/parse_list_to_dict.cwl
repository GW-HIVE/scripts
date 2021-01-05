class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: parse_list
baseCommand: []
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
requirements:
  - class: DockerRequirement
    dockerPull: list-parser-script
    dockerOutputDirectory: \src
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.to_parse)
  - class: InlineJavascriptRequirement
stdout: dict.txt
