function add(numbers) {
    // Step 1: Handle an empty string
    if (numbers === "") {
        return 0;
    }

    // Step 2: Handle custom delimiter (//[delimiter]\n[numbers...])
    if (numbers.startsWith("//")) {
        const delimiterIndex = numbers.indexOf("\n");
        const delimiter = numbers.slice(2, delimiterIndex); // Extract custom delimiter
        numbers = numbers.slice(delimiterIndex + 1); // Remove the delimiter part

        // Replace the custom delimiter with commas
        numbers = numbers.replace(new RegExp(delimiter, 'g'), ',');
    }

    // Step 3: Replace newlines with commas and split the numbers
    const numberArray = numbers.replace(/\n/g, ",").split(',');

    let sum = 0;
    let negativeNumbers = [];

    // Step 4: Process the numbers
    for (let number of numberArray) {
        const num = parseInt(number, 10);

        // Step 5: Handle negative numbers
        if (num < 0) {
            negativeNumbers.push(num);
        } else {
            sum += num;
        }
    }

    // Step 6: If there are negative numbers, throw an exception
    if (negativeNumbers.length > 0) {
        throw new Error("Negative numbers not allowed: " + negativeNumbers.join(","));
    }

    return sum;
}
