function arrayDivision(arr) {
    let result = [];
    
    for (let i = 0; i < arr.length; i++) {
        try {
            let divisionResult;
            if (i === arr.length - 1) {
                divisionResult = arr[i] / arr[0];
            } else {
                divisionResult = arr[i] / arr[i + 1];
            }
            
            result.push(divisionResult);
        } catch (error) {
            console.log(`Warning: Division by zero encountered for element at index ${i}. Skipping operation.`);
        }
    }
    
    return result;
}

let array = [9, 33, 0, 7, 2, 82, 771];

let result = arrayDivision(array);

console.log(result);
