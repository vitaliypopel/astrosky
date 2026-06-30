import { api } from '@/api'
import type { Constellation } from '@/api/constellation/types'

export const getConstellations = async (): Promise<Constellation[]> => {
  const response = await api.get<Constellation[]>('/constellations/')

  return response.data
}

export const getConstellation = async (id: number): Promise<Constellation> => {
  const response = await api.get<Constellation>(`/constellations/${id}/`)

  return response.data
}
