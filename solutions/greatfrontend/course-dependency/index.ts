export default function canCompleteCourse(
  courses: number,
  prerequisites: number[][],
): boolean {
  const adj: number[][] = Array(courses)
    .fill(null)
    .map(() => []);

  const indegree: number[] = Array(courses).fill(0);

  for (const [a, b] of prerequisites) {
    adj[b].push(a);
    indegree[a] += 1;
  }

  const queue: number[] = [];
  for (let i = 0; i < courses; ++i) {
    if (indegree[i] == 0) {
      queue.push(i);
    }
  }

  let count = 0;
  while (queue.length > 0) {
    const course = queue.shift();
    if (course == null) continue;
    count++;

    for (const neighbor of adj[course]) {
      indegree[neighbor]--;
      if (indegree[neighbor] == 0) {
        queue.push(neighbor);
      }
    }
  }

  return courses == count;
}
