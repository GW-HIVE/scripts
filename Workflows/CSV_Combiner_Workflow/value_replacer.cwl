class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: value_replacer
baseCommand:
  - python ../python/csv_value_replacer.py
inputs:
  - id: header_index
    type: int
    inputBinding:
      position: 0
  - id: mapping_value
    type: File
    inputBinding:
      position: 1
  - id: original_csv
    type: File
    inputBinding:
      position: 2
  - id: filename
    type: string
    inputBinding:
      position: 3
outputs:
  - id: parsed_file
    type: File
    outputBinding:
      glob: $(inputs.filename + '.csv')
requirements:
  - class: DockerRequirement
    dockerOutputDirectory: \src
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.mapping_value)
      - $(inputs.original_csv)
  - class: InlineJavascriptRequirement
stdout: $(inputs.filename + '.csv')
