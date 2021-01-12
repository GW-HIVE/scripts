class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: parse_file
baseCommand:
  - python ../python/csv_to_list_parser.py
inputs:
  - id: to_parse
    type: File
    inputBinding:
      position: 1
outputs:
  - id: parsed_file
    type: File
    outputBinding:
      glob: parsed_file.txt
arguments:
  - position: 0
    valueFrom: '-i'
requirements:
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.to_parse)
  - class: InlineJavascriptRequirement
stdout: parsed_file.txt
