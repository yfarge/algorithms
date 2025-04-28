export default function isStringPalindrome(str: string): boolean {
  let left = 0;
  let right = str.length - 1;

  while (left < right) {
    if (!isAlnum(str[left].toLowerCase())) {
      left++;
      continue;
    }

    if (!isAlnum(str[right].toLowerCase())) {
      right--;
      continue;
    }

    if (str[left] != str[right]) {
      return false;
    }

    left++;
    right--;
  }

  return true;
}

function isAlnum(char: string): boolean {
  const code = char.charCodeAt(0);
  return (
    (code >= 48 && code <= 57) ||
    (code >= 65 && code <= 90) ||
    (code >= 97 && code <= 122)
  );
}
