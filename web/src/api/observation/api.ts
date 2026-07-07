import { api } from '@/api'
import type { Observation, ObserveManyQuery, ObserveQuery } from '@/api/observation/types'

export const observe = async (query: ObserveQuery): Promise<Observation> => {
  const response = await api.post<Observation>('/observe/', query)

  return response.data
}

export const observeMany = async (query: ObserveManyQuery): Promise<Observation> => {
  const response = await api.post<Observation>('/observe/many/', query)

  return response.data
}
