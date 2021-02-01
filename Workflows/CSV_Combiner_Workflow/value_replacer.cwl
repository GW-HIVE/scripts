class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: value_replacer
baseCommand:
  - python
inputs:
  - id: header_index
    type: int
    inputBinding:
      position: 1
  - id: mapping_value
    type: File
    inputBinding:
      position: 3
  - id: original_csv
    type: File
    inputBinding:
      position: 5
  - id: filename
    type: string
  - id: script
    type: File
    inputBinding:
      position: -1
outputs:
  - id: parsed_file
    type: File
    outputBinding:
      glob: $(inputs.filename + '.csv')
arguments:
  - position: 0
    valueFrom: '-v'
  - position: 2
    valueFrom: '-d'
  - position: 4
    valueFrom: '-i'
requirements:
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.mapping_value)
      - $(inputs.original_csv)
      - $(inputs.script)
  - class: InlineJavascriptRequirement
stdout: $(inputs.filename + '.csv')
