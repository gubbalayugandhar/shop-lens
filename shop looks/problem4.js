function lastManStanding(n) {
    
    let circle = Array.from({ length: n }, (_, i) => i + 1);

    let index = 0;
    while (circle.length > 1) {
        
        index = (index + 1) % circle.length;
        circle.splice(index, 1);
    }

    return circle[0];
}

let survivor = lastManStanding(100);
console.log("The last man standing is:", survivor);
