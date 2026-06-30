export interface Constellation {
  id: number

  name: string
  code: string

  ra: number
  dec: number

  area: number
  area_pct: number

  season: string

  eq: string
  ecl: string
  mw: string | null

  quad: string

  origin: string
}
