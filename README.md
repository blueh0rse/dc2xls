# dc2xls

Transform your Dependency Check reports into XLS.

## Usage

`$ python3 dc2xls.py --input <input_file> --ouput <output_file>`

## How it works?

The script parses your HTML Dependency-Check report with BeautifulSoup and lists every vulnerable dependencies with their details.

- For each dependency it extracts:
    - CVE
    - CWE
    - Description
    - Score
    - Severity

It generates then a table with all the data and create an XLS file.

## Output format

The table is as the following:

| Dependency       |      CVE      |  CWE   | Score | Severity | Description |
| ---------------- | :-----------: | :----: | :---- | :------: | :---------- |
| dependency@0.0.0 | CVE-0000-0000 | CWE 14 | 9.5   | Critical | Description |
| dependency@0.0.0 | CVE-0000-0000 | CWE 14 | 9.5   | Critical | Description |
| dependency@0.0.0 | CVE-0000-0000 | CWE 14 | 9.5   | Critical | Description |

## Roadmap

- [ ] Transform HTML report into XLS file 🚧
  - [ ] Generate table
  - [ ] Generate xls
  - [ ] Clean input file
- [ ] Provide an example HTML report
- [ ] Support multiple HTML input files
- [ ] Add metadata
- [ ] Support XML input report format
- [ ] Provide an example XML report
- [ ] Support multiple format input file
- [ ] Can generate different views
