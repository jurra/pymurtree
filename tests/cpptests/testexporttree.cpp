#include <gtest/gtest.h>
#include "exporttree.h"

// Demonstrate some basic assertions.
TEST(ExportText, NewFileIsCreated) {
  
  // Create label nodes
	MurTree::DecisionNode* c1 = MurTree::DecisionNode::CreateLabelNode(1);
	MurTree::DecisionNode* c2 = MurTree::DecisionNode::CreateLabelNode(2);
	MurTree::DecisionNode* c3 = MurTree::DecisionNode::CreateLabelNode(3);

	// Create feature nodes
	MurTree::DecisionNode* f3 = MurTree::DecisionNode::CreateFeatureNodeWithNullChildren(3);
	MurTree::DecisionNode* f7 = MurTree::DecisionNode::CreateFeatureNodeWithNullChildren(7);
	
	// Assign children
	f7->left_child_ = c1;
	f7->right_child_ = f3;
	f3->left_child_ = c2;
	f3->right_child_ = c3;

	//ExportTree::exportText(f7, "~/outputfile.txt");
	ExportTree::exportText(f7);

	// ExportTree::exportDOT(f7, "outputfile.txt");

	delete c1;
	delete c2;
	delete c3;
	delete f3;
	delete f7;

  // Expect two strings not to be equal.
  EXPECT_STRNE("hello", "world");
  // Expect equality.
  EXPECT_EQ(7 * 6, 43);
}