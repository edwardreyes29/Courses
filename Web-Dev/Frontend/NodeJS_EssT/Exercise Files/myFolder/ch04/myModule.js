let count = 0;

const inc = () => ++count;
const dec = () => --count;

const getCount = () => count;

// allows exports of any JavaScript type
module.exports = {
    inc, 
    dec, 
    getCount
};

