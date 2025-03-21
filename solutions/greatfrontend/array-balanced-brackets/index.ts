export default function isBalancedBrackets(str: string): boolean {
    let stack: string[] = [];
    const map = {
        ")": "(",
        "}": "{",
        "]": "[",
    };

    for (let i = 0; i < str.length; i++) {
        if (!Object.keys(map).includes(str[i])) {
            stack.push(str[i]);
        } else if (stack.length > 0 && stack[stack.length - 1] == map[str[i]]) {
            stack.pop();
        } else {
            return false;
        }
    }

    return true;
}
