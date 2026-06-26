import { api } from '@/api'
import type { PaginatedResponse } from '@/api/pagination/types'
import type { StarQueryParams } from '@/api/star/types'
import type { Star } from '@/api/star/types'

export const getStars = async (params?: StarQueryParams): Promise<PaginatedResponse<Star>> => {
  const response = await api.get<PaginatedResponse<Star>>('/stars/', { params })

  return response.data
}

export const getStar = async (id: number): Promise<Star> => {
  const response = await api.get<Star>(`/stars/${id}/`)

  return response.data
}
