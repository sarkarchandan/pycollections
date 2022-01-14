iter_for:
	python iter/basic_iterators.py iter_for
call_next:
	python iter/basic_iterators.py call_next
level_order:
	python iter/basic_iterators.py level_order
level_order_iterable:
	python iter/basic_iterators.py level_order_iterable
pre_order_iterable:
	python iter/basic_iterators.py pre_order_iterable
in_order_iterable:
	python iter/basic_iterators.py in_order_iterable
filtering_iterator:
	python iter/filter_iterators.py
transform_iterator:
	python iter/transform_iterators.py
iterable_as_is:
	python iter/iterable.py iterable_as_is
iterator_from_iterable:
	python iter/iterable.py iterator_from_iterable
alternative_iterable:
	python iter/alternative_iterable.py
generate_sequence_from_file:
	python iter/extended_iter.py generate_sequence_from_file
generate_indefinite_timestamps:
	python iter/extended_iter.py generate_indefinite_timestamps
test_sorted_frozen:
	python coll/test_frozen_set.py
lint:
	pylint coll iter
