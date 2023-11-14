enum Operation {
  Add = "add",
  Subtract = "subtract",
  Multiply = "multiply",
  Divide = "divide",
}

type Calculator = (a: number, b: number) => number;

// Factory function to create calculator
// What is a factory function? https://www.youtube.com/watch?v=ImwrezYhw4w
function createCalculator(operation: Operation): Calculator {
  return function (a: number, b: number) {
    switch (operation) {
      case Operation.Add:
        return a + b;
      case Operation.Subtract:
        return a - b;
      case Operation.Multiply:
        return a * b;
      case Operation.Divide:
        return a / b;
      default:
        throw new Error(`Invalid operation: ${operation}`);
    }
  };
}

const add = createCalculator(Operation.Add);
console.log(add(2, 3)); // Output: 5

const subtract = createCalculator(Operation.Subtract);
console.log(subtract(5, 3)); // Output: 2

const multiply = createCalculator(Operation.Multiply);
console.log(multiply(2, 3)); // Output: 6

const divide = createCalculator(Operation.Divide);
console.log(divide(6, 3)); // Output: 2