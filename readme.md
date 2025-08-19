# Assembler Simulator Performance and Verification Suite

A comprehensive testing framework for evaluating student implementations of assemblers and simulators. This framework provides automated testing capabilities with both simple and complex test cases to assess the correctness of assembly language processors and CPU simulators.

## Overview

This project provides a structured testing environment for:
- **Assembler**: Converts assembly code to machine code
- **Simulator**: Executes machine code and generates execution traces

The framework includes independent test suites for both components, allowing focused evaluation of each part of the system.

## Project Structure

```
├── src/
│   └── main.py                 # Main testing framework
├── tests/
│   ├── assembly/               # Assembler test cases
│   │   ├── simpleBin/         # Simple assembly test files
│   │   ├── hardBin/           # Complex assembly test files
│   │   ├── errorGen/          # Error generation test files
│   │   ├── bin_s/             # Expected machine code (simple tests)
│   │   ├── bin_h/             # Expected machine code (hard tests)
│   │   ├── user_bin_s/        # Student assembler output (simple)
│   │   └── user_bin_h/        # Student assembler output (hard)
│   ├── bin/                   # Student simulator traces
│   └── traces/                # Expected simulator traces
├── SimpleAssembler/           # Place your Assembler.py here
└── SimpleSimulator/           # Place your Simulator.py here
```

## Scoring System (2024)

### Assembler Tests
- **Simple Tests**: 10 tests × 0.1 points each = **1.0 points**
- **Hard Tests**: 5 tests × 0.2 points each = **1.0 points**
- **Total Assembler Score**: **2.0 points**

### Simulator Tests
- **Simple Tests**: 5 tests × 0.4 points each = **2.0 points**
- **Hard Tests**: 5 tests × 0.8 points each = **4.0 points**
- **Total Simulator Score**: **6.0 points**

**Maximum Total Score**: **8.0 points**

## Getting Started

### Prerequisites
- Python 3.x
- Your assembler and simulator implementations

### File Requirements
- All input and output files must use `.txt` extensions
- File names are case-sensitive

## Usage Instructions

### Setting Up Your Assembler

1. **Rename your assembler file** to `Assembler.py`
2. **Place it in the `SimpleAssembler/` folder**
3. **Ensure your assembler follows this format**:
   ```bash
   python3 Assembler.py input_assembly_code_file_path output_machine_code_file_path
   ```

#### Running Assembler Tests
```bash
# Linux users
python3 src/main.py --no-sim --linux

# Windows users
python3 src\main.py --no-sim --windows
```

### Setting Up Your Simulator

1. **Rename your simulator file** to `Simulator.py`
2. **Place it in the `SimpleSimulator/` folder**
3. **Ensure your simulator follows this format**:
   ```bash
   python3 Simulator.py input_machine_code_file_path output_trace_file_path
   ```

#### Running Simulator Tests
```bash
# Linux users
python3 src/main.py --no-asm --linux

# Windows users
python3 src\main.py --no-asm --windows
```

### Running All Tests
```bash
# Linux users
python3 src/main.py --linux

# Windows users
python3 src\main.py --windows
```

## Test Categories

### Assembler Tests
- **Simple Tests** (`simpleBin/`): Basic assembly instructions and operations
- **Hard Tests** (`hardBin/`): Complex assembly programs with advanced features
- **Error Tests** (`errorGen/`): Invalid assembly code to test error handling

### Simulator Tests
- **Simple Tests**: Basic instruction execution and state changes
- **Hard Tests**: Complex programs with multiple instruction types and edge cases

## Test Files Explanation

### Assembly Test Structure
- `tests/assembly/simpleBin/` → Input assembly files for simple tests
- `tests/assembly/bin_s/` → Expected machine code output for simple tests
- `tests/assembly/user_bin_s/` → Your assembler's output for simple tests
- `tests/assembly/hardBin/` → Input assembly files for hard tests  
- `tests/assembly/bin_h/` → Expected machine code output for hard tests
- `tests/assembly/user_bin_h/` → Your assembler's output for hard tests

### Simulator Test Structure
- `tests/traces/` → Expected simulator execution traces
- `tests/bin/` → Your simulator's generated traces

## Important Notes

- This framework is designed **for Python users only**
- Tests for assembler and simulator are **completely independent**
- Ensure your code handles file paths correctly for your operating system
- All output files will be automatically generated in the appropriate directories
- Make sure your implementations can handle the specified command-line argument format

## Troubleshooting

### Common Issues
1. **File not found errors**: Ensure file paths and extensions are correct
2. **Permission errors**: Check that the framework has write permissions in test directories
3. **Import errors**: Verify your Python environment and file locations
4. **Path separator issues**: Use the correct flag for your operating system (`--linux` vs `--windows`)

### Debug Tips
- Check that your files are named exactly `Assembler.py` and `Simulator.py`
- Verify file locations in `SimpleAssembler/` and `SimpleSimulator/` folders
- Ensure your code accepts command-line arguments in the specified format

## Support

If you encounter issues with the testing framework, please check:
1. File naming conventions
2. Directory structure
3. Command-line argument handling in your implementations
4. Operating system compatibility flags

---

**Good luck with your implementation!**

