import pdb
from models.munro import Munro
from models.climber import Climber
from models.bag import Bag

import repositories.munro_repository as munro_repository
import repositories.climber_repository as climber_repository
import repositories.bag_repository as bag_repository

bag_repository.delete_all()
munro_repository.delete_all()
climber_repository.delete_all()

climber1 = Climber('Janek Metelski')
climber_repository.save(climber1)

climber2 = Climber('Jessica Metelski')
climber_repository.save(climber2)

climber3 = Climber('Jimmy Saville')
climber_repository.save(climber3)

munro1 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro2 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

bag1 = Bag(climber1, munro1, 'great climb, enjoyed it')
bag_repository.save(bag1)

bag2 = Bag(climber3, munro1, 'knackered, too old for this shit!')
bag_repository.save(bag2)

bag3 = Bag(climber1, munro2, 'had a super time')
bag_repository.save(bag3)

bag4 = Bag(climber2, munro2, 'too crowded!')
bag_repository.save(bag4)

print(climber_repository.munros(climber1))
print(munro_repository.climbers(munro1))
pdb.set_trace()