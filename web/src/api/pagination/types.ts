export interface PaginatedResponse<T> {
  const: number
  next: string | null
  previous: string | null
  results: T[]
}
