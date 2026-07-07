import type { Constellation } from '@/api/constellation/types'

export interface Star {
  id: number

  constellation: Constellation | null

  hip: number | null
  hd: number | null
  hr: number | null
  gl: string
  bf: string

  name: string

  names: string[]

  bayer: string
  flam: number | null

  ra: number
  dec: number

  dist: number | null

  mag: number
  absmag: number | null

  spect: string
  ci: number | null

  pmra: number | null
  pmdec: number | null

  rv: number | null

  lum: number | null
}

export interface StarQueryParams {
  page?: number
}
