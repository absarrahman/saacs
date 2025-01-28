import { z } from 'zod'
// import { auth, common } from 'saacs'

import { useChaincode } from '~/server/utils/useChaincode'

const querySchema = z.object({
  collectionId: z.string(),
})

export default defineEventHandler(async (event) => {
  const cc = await useChaincode(event)

  const query = await getValidatedQuery(event, querySchema.parse)

  const result = await cc.service.listByAttrs(
    new pb.ListByAttrsRequest({
      key: new pb.ItemKey({
        collectionId: query.collectionId,
        itemKeyParts: [query.collectionId],
        itemType: pb.UserCollectionRoles.typeName,
      }),
      numAttrs: 1,
    }),
  )

  // console.log(result);
  const UserRoles = result.items.map((i) => {
    const s = new pb.UserCollectionRoles()
    i.value?.unpackTo(s)
    return s.toJson({ emitDefaultValues: true })
  })

  console.log({ UserRoles })
  return UserRoles
})
