// Approach:
// Return a function that ignores any arguments and always returns "Hello World".
//
// Time: O(1)
// Space: O(1)

function createHelloWorld() {
    return function (...args): string {
        return "Hello World";
    };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
