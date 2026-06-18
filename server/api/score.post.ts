type ScoreRequestBody = {
  company_id: string
  dimensions: {
    governance: number
    innovation: number
    operations: number
    finance: number
    sustainability: number
  }
}

export default defineEventHandler(async (event) => {
  const { scoreServiceUrl } = useRuntimeConfig(event)
  const body = await readBody<ScoreRequestBody>(event)

  return await $fetch(`${scoreServiceUrl}/score`, {
    method: 'POST',
    body,
  })
})
