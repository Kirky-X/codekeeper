"""Test fixtures for language handler tests."""

import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def sample_python_code():
    return '''#!/usr/bin/env python3
# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.

"""Sample Python module for testing."""

def hello_world():
    """A simple hello world function."""
    print("Hello, World!")


class Calculator:
    """A simple calculator class."""

    def __init__(self, initial_value: int = 0):
        self.value = initial_value

    def add(self, x: int) -> int:
        """Add x to the calculator value."""
        self.value += x
        return self.value
'''


@pytest.fixture
def sample_rust_code():
    return """// Copyright (c) 2025 Author. All rights reserved.
// Licensed under the MIT License.

// Sample Rust module for testing.

pub struct Calculator {
    value: i32,
}

impl Calculator {
    pub fn new(initial_value: i32) -> Self {
        Calculator { value: initial_value }
    }

    pub fn add(&mut self, x: i32) -> i32 {
        self.value += x;
        self.value
    }
}
"""


@pytest.fixture
def sample_java_code():
    return """// Copyright (c) 2025 Author. All rights reserved.
// Licensed under the MIT License.

// Sample Java class for testing.

public class Calculator {
    private int value;

    public Calculator() {
        this.value = 0;
    }

    public Calculator(int initialValue) {
        this.value = initialValue;
    }

    public int add(int x) {
        this.value += x;
        return this.value;
    }
}
"""


@pytest.fixture
def sample_go_code():
    return """// Copyright (c) 2025 Author. All rights reserved.
// Licensed under the MIT License.

package main

type Calculator struct {
    value int
}

func NewCalculator(initialValue int) *Calculator {
    return &Calculator{value: initialValue}
}

func (c *Calculator) Add(x int) int {
    c.value += x
    return c.value
}

func standaloneFunction() int {
    return 42
}
"""


@pytest.fixture
def temp_python_file(sample_python_code):
    """Create a temporary Python file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(sample_python_code)
        temp_path = f.name
    yield Path(temp_path)
    os.unlink(temp_path)


@pytest.fixture
def temp_rust_file(sample_rust_code):
    """Create a temporary Rust file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".rs", delete=False) as f:
        f.write(sample_rust_code)
        temp_path = f.name
    yield Path(temp_path)
    os.unlink(temp_path)


@pytest.fixture
def temp_java_file(sample_java_code):
    """Create a temporary Java file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".java", delete=False) as f:
        f.write(sample_java_code)
        temp_path = f.name
    yield Path(temp_path)
    os.unlink(temp_path)


@pytest.fixture
def temp_go_file(sample_go_code):
    """Create a temporary Go file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".go", delete=False) as f:
        f.write(sample_go_code)
        temp_path = f.name
    yield Path(temp_path)
    os.unlink(temp_path)


@pytest.fixture
def sample_typescript_code():
    return """// Copyright (c) 2025 Author. All rights reserved.
// Licensed under the MIT License.

interface CalculatorInterface {
    add(x: number): number;
    value: number;
}

type CalculatorState = {
    initialized: boolean;
    lastOperation: string;
};

class Calculator implements CalculatorInterface {
    public value: number = 0;
    private readonly precision: number;

    constructor(precision: number = 2) {
        this.precision = precision;
    }

    async add(x: number): Promise<number> {
        this.value += x;
        return this.value;
    }

    subtract(x: number): number {
        this.value -= x;
        return this.value;
    }

    getValue(): number {
        return this.value;
    }
}

function standaloneFunction(): string {
    return "Hello from TypeScript";
}

const arrowFunction = (x: number): number => {
    return x * 2;
};

function withCallback(callback: (result: number) => void): void {
    callback(this.value);
}
"""


@pytest.fixture
def sample_cpp_code():
    return """// Copyright (c) 2025 Author. All rights reserved.
// Licensed under the MIT License.

#include <iostream>
#include <string>

namespace MathUtils {

class Calculator {
private:
    int value;
    const int precision;

public:
    Calculator(int initialValue = 0, int prec = 2) : value(initialValue), precision(prec) {}

    int add(int x) {
        value += x;
        return value;
    }

    int subtract(int x) {
        value -= x;
        return value;
    }

    int getValue() const {
        return value;
    }

    static int multiply(int a, int b) {
        return a * b;
    }
};

struct Point {
    int x;
    int y;

    Point(int xCoord = 0, int yCoord = 0) : x(xCoord), y(yCoord) {}

    int distance() const {
        return std::sqrt(x * x + y * y);
    }
};

} // namespace MathUtils

int standaloneFunction() {
    return 42;
}

template<typename T>
T maxValue(T a, T b) {
    return a > b ? a : b;
}
"""


@pytest.fixture
def temp_typescript_file(sample_typescript_code):
    """Create a temporary TypeScript file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".ts", delete=False) as f:
        f.write(sample_typescript_code)
        temp_path = f.name
    yield Path(temp_path)
    os.unlink(temp_path)


@pytest.fixture
def temp_cpp_file(sample_cpp_code):
    """Create a temporary C++ file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".cpp", delete=False) as f:
        f.write(sample_cpp_code)
        temp_path = f.name
    yield Path(temp_path)
    os.unlink(temp_path)


@pytest.fixture
def all_temp_files(temp_python_file, temp_rust_file, temp_java_file, temp_go_file):
    """Provide all temporary files."""
    return {
        "python": temp_python_file,
        "rust": temp_rust_file,
        "java": temp_java_file,
        "go": temp_go_file,
    }
