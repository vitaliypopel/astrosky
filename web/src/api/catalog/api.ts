import { api } from '@/api'
import type { Catalog } from '@/api/catalog/types'

export const getCatalogs = async (): Promise<Catalog[]> => {
  const response = await api.get<Catalog[]>('/catalogs/')

  return response.data
}

export const getCatalog = async (code: string): Promise<Catalog> => {
  const response = await api.get<Catalog>(`/catalogs/${code}/`)

  return response.data
}
